/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.LinkedList;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Processor4 {
    
    private LinkedList<Integer> list = new LinkedList<Integer>();
    private final int LIMIT = 10;
    private Object lock = new Object();
    
    public void produce() throws InterruptedException {
        int value = 0;
        
        while (true) {
            synchronized (lock) {
                while (list.size() == LIMIT) {
                    lock.wait();
                }
                list.add(value++);
            }
        }
    }
    
    public void consume() throws InterruptedException {
        
        Random random = new Random();
        
        while (true) {
            synchronized (lock) {
                while (list.size() == 0) {
                    lock.wait();
                }
                System.out.print("List size is: " + list.size());
                int value = list.removeFirst();
                System.out.println(", value is: " + value);
                lock.notify();
            }
            Thread.sleep(random.nextInt(1000));
        }
        
    }
    
}

public class ThreadDemo11 {
    
    public static void main(String[] args) throws InterruptedException {
        
        final Processor4 processor = new Processor4();
        
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor.produce();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo11.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            
        });
    
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor.consume();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo10.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
    }
    
}
