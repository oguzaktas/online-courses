/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

import java.util.Random;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author oguz
 */

class Runner2 {
    
    private Account a1 = new Account();
    private Account a2 = new Account();
    
    private Lock lock1 = new ReentrantLock();
    private Lock lock2 = new ReentrantLock();
    
    private void acquireLocks(Lock firstLock, Lock secondLock) {
        while (true) {
            // Acquire locks
            boolean gotFirstLock = false;
            boolean gotSecondLock = false;
            try {
                gotFirstLock = firstLock.tryLock();
                gotSecondLock = secondLock.tryLock();
            } finally {
                if (gotFirstLock && gotSecondLock) {
                    return;
                }
                if (gotFirstLock) {
                    firstLock.unlock();
                }
                if (gotSecondLock) {
                    secondLock.unlock();
                }
            }
            // Locks not acquired
        }
    }
    
    public void firstThread() {
        Random random = new Random();
        
        for (int i = 0; i < 10000; i++) {
            acquireLocks(lock1, lock2);
            try {
                Account.transfer(a1, a2, random.nextInt(100));
            } finally {
                lock1.unlock();
                lock2.unlock();
            }
        }
    }
    
    public void secondThread() {
        Random random = new Random();
        
        for (int i = 0; i < 10000; i++) {
            // if locks in different orders -> deadlock occurs
            acquireLocks(lock2, lock1);
            try {
                Account.transfer(a2, a1, random.nextInt(100));
            } finally {
                lock1.unlock();
                lock2.unlock();
            }
        }
    }
    
    public void finished() {
        System.out.println("Account 1 balance: " + a1.getBalance());
        System.out.println("Account 2 balance: " + a2.getBalance());
        System.out.println("Total balance: " + (a1.getBalance() + a2.getBalance()));
    }
    
}

class Account {
    
    private int balance = 10000;
    
    public void deposit(int amount) {
        balance += amount;
    }
    
    public void withdraw(int amount) {
        balance -= amount;
    }
    
    public int getBalance() {
        return balance;
    }
    
    public static void transfer(Account a1, Account a2, int amount) {
        a1.withdraw(amount);
        a2.deposit(amount);
    }
    
}

public class ThreadDemo13 {
    
    public static void main(String[] args) throws InterruptedException {
        
        final Runner2 runner = new Runner2();
        
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                runner.firstThread();
            }
            
        });
    
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                runner.secondThread();
            }
            
        });
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
        runner.finished();
    }
    
}