/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.io.IOException;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */
public class ThreadDemo15 {
    
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ExecutorService executor = Executors.newCachedThreadPool();
        Future<?> future =  executor.submit(new Callable<Void>() {
            @Override
            public Void call() throws Exception {
                Random random = new Random();
                int duration = random.nextInt(4000);
                if (duration > 2000) {
                    throw new IOException("Sleeping for too long.");
                }
                System.out.println("Starting...");
                try {
                    Thread.sleep(duration);
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo15.class.getName()).log(Level.SEVERE, null, ex);
                }
                System.out.println("Finished.");
                return null;
            }
        });
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.DAYS);
    
        try {
            System.out.println("Result is: " + future.get());
        } catch (InterruptedException ex) {
            Logger.getLogger(ThreadDemo15.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ExecutionException ex) {
            IOException e = (IOException) ex.getCause();
            System.out.println(ex.getMessage());
        }
    }

}
