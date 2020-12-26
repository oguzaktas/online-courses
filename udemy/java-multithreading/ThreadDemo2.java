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

class Runner2 implements Runnable {

    @Override
    public void run() {
        // throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
        for (int i = 0; i < 10; i++) {
            System.out.println("Hello " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Logger.getLogger(Runner.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
    
}

public class ThreadDemo2 {
    
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runner2());
        Thread t2 = new Thread(new Runner2());
        t1.start();
        t2.start();
    }
    
}
