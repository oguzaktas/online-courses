/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication3;

import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Processor extends Thread {
    
    private volatile boolean running = true;
    // volatile keyword is used for prevent threads caching variables when they are not changed from within that thread
    
    public void run() {
        while (running) {
            System.out.println("Hello");
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Logger.getLogger(Processor.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
    
    public void shutdown() {
        running = false;
    }
}

public class ThreadDemo4 {
    public static void main(String[] args) {
        Processor proc1 = new Processor();
        proc1.start(); // To terminate: threasd interruptions
        System.out.println("Press return to shutdown...");
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
        proc1.shutdown();
    }
}
