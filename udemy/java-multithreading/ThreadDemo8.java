/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Processor2 implements Runnable {
    
    private CountDownLatch latch;
    
    public Processor2(CountDownLatch latch) {
        this.latch = latch;
    }

    @Override
    public void run() {
        System.out.println("Started.");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException ex) {
            Logger.getLogger(Processor2.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        latch.countDown();
    }
    
}

public class ThreadDemo8 {
    
    public static void main(String[] args) {
        CountDownLatch latch = new CountDownLatch(3); // One or more threads wait until the latch reaches countdown 0.
        // CountDownLatch is thread-safe class, so not necessary to use synchronized keyword.
        
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        for (int i = 0; i < 3; i++) {
            executor.submit(new Processor2(latch));
        }
        try {
            latch.await();
        } catch (InterruptedException ex) {
            Logger.getLogger(ThreadDemo8.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        System.out.println("Completed.");
    }
    
}
