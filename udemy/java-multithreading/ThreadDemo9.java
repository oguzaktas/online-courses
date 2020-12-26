/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */
public class ThreadDemo9 {
    
    private static BlockingQueue queue = new ArrayBlockingQueue<Integer>(10);
        
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    producer();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo9.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        });
        
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    consumer();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo9.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
    }
    
    private static void producer() throws InterruptedException {
        Random random = new Random();
        while (true) {
            queue.put(random.nextInt(100));
        }
    }
    
    private static void consumer() throws InterruptedException {
        Random random = new Random();
        while (true) {
            Thread.sleep(100);
            if (random.nextInt(10) == 0) {
                Integer value = (Integer) queue.take();
                System.out.println("Taken value: " + value + ", queue size is: " + queue.size());
            }
        }
    }
    
}

// Low-level threading techniques with synchronized, notify, wait keywords