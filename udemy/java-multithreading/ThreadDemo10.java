/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Processor3 {
    public void produce() throws InterruptedException {
        synchronized (this) { // intrinsic lock
            System.out.println("Producer thread running...");
            wait();
            System.out.println("Resumed.");
            
        }
    }
    
    public void consume() throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        Thread.sleep(2000);
        
        synchronized (this) {
            System.out.println("Waiting for return key.");
            scanner.nextLine();
            System.out.println("Return key pressed.");
            notify();
            Thread.sleep(5000);
        }
    }
}

public class ThreadDemo10 {
    
    public static void main(String[] args) throws InterruptedException {
        
        final Processor3 processor = new Processor3();
        
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor.produce();
                } catch (InterruptedException ex) {
                    Logger.getLogger(ThreadDemo10.class.getName()).log(Level.SEVERE, null, ex);
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
