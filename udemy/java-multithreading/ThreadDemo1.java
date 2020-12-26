/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication3;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Runner extends Thread {

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("Hello " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Logger.getLogger(Runner.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        // super.run(); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public synchronized void start() {
        super.start(); //To change body of generated methods, choose Tools | Templates.
    }
    
}

public class ThreadDemo1 {
    
    public static void main(String[] args) {
        Runner runner1 = new Runner();
        runner1.start();
        Runner runner2 = new Runner(); // Both runner are running concurrently. With threads you can run codes simultaneously.
        runner2.start();
    }
    
}
