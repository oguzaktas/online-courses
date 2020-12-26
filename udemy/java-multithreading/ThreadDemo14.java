/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Connection {
    
    private static Connection instance = new Connection();
    
    private Semaphore s = new Semaphore(10, true);
    
    private int connections = 0;
    
    private Connection() {
        
    }
    
    public static Connection getInstance() {
        return instance;
    }
    
    public void connect() throws InterruptedException {
        try {
            s.acquire();
        } catch (InterruptedException ex) {
            Logger.getLogger(ThreadDemo14.class.getName()).log(Level.SEVERE, null, ex);
        }

        try {
            doConnect();
        } finally {
            s.release();
        }
    }
    
    public void doConnect() throws InterruptedException {
        
        synchronized (this) {
            connections++;
            System.out.println("Current connections: " + connections);
        }
        
        Thread.sleep(2000);
        
        synchronized (this) {
            connections--;
        }
        
    }
    
}

public class ThreadDemo14 {
    
    public static void main(String[] args) throws InterruptedException {
        /*
        Semaphore s = new Semaphore(1);
        s.release();
        s.acquire();
        System.out.println("Available permits: " + s.availablePermits());
        */

        Connection.getInstance().connect();
        
        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 0; i < 200; i++) {
            executor.submit(new Runnable() {
                @Override
                public void run() {
                    try {
                        Connection.getInstance().connect();
                    } catch (InterruptedException ex) {
                        Logger.getLogger(ThreadDemo14.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
                
            });
        }
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.DAYS);
    }
    
}
