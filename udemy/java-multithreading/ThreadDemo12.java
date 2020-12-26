/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.Scanner;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Runner {
    
    private int count = 0;
    private Lock lock = new ReentrantLock();
    private Condition cond = lock.newCondition();
    
    private void increment() {
        for (int i = 0; i < 10000; i++) {
            count++;
        }
    }
    
    public void firstThread() throws InterruptedException {
        lock.lock();
        System.out.println("Waiting...");
        cond.await();
        System.out.println("Woken up!");
        try {
            increment();
        } finally {
            lock.unlock();
        }
    }
    
    public void secondThread() throws InterruptedException {
        Thread.sleep(1000);
        lock.lock();
        
        System.out.println("Press the return key!");
        new Scanner(System.in).nextLine();
        System.out.println("Got return key!");
        
        cond.signal();
        
        try {
            increment();
        } finally {
            lock.unlock();
        }
    }
    
    public void finished() {
        System.out.println("Count is: " + count);
    }
    
}

public class ThreadDemo12 {
    
    public static void main(String[] args) throws InterruptedException {
        
        final Runner runner = new Runner();
        
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    runner.firstThread();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo12.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            
        });
    
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    runner.secondThread();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo12.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
        runner.finished();
    }
    
}
