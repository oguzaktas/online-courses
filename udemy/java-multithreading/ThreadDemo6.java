/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */
public class ThreadDemo6 {
    
    private static Random random = new Random();
    
    private static Object lock1 = new Object();
    private static Object lock2 = new Object();
    
    private static List<Integer> list1 = new ArrayList<Integer>();
    private static List<Integer> list2 = new ArrayList<Integer>();
    
    public static void stageOne() {
        synchronized (lock1) {
            try {
                Thread.sleep(1);
            } catch (InterruptedException ex) {
                Logger.getLogger(ThreadDemo6.class.getName()).log(Level.SEVERE, null, ex);
            }

            list1.add(random.nextInt(100));
        }
    }

    public static void stageTwo() {
        synchronized (lock2) {
            try {
                Thread.sleep(1);
            } catch (InterruptedException ex) {
                Logger.getLogger(ThreadDemo6.class.getName()).log(Level.SEVERE, null, ex);
            }

            list2.add(random.nextInt(100));
        }
    }

    public static void process() {
        for (int i = 0; i < 1000; i++) {
            stageOne();
            stageTwo();
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Starting...");
        long start = System.currentTimeMillis();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                process();
            }
            
        });
        t1.start();
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                process();
            }
            
        });
        t2.start();
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException ex) {
            Logger.getLogger(ThreadDemo6.class.getName()).log(Level.SEVERE, null, ex);
        }
        long end = System.currentTimeMillis();
        System.out.println("Time take: " + (end - start));
        System.out.println("List1: " + list1.size() + ", List2: " + list2.size());
    }
    
}
