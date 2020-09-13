
/**
 * Write a description of Tester here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */

import java.util.*;
import edu.duke.*;

public class Tester {
    
    public void testGetFollows() {
        MarkovOne markov = new MarkovOne();
        markov.setTraining("this is a test yes this is a test.");
        
        String key = "o";
        ArrayList<String> follows = markov.getFollows(key);
        System.out.println("Letters that follow \"" + key + "\": " + follows);
        System.out.println("There are " + follows.size() + " letters that follow \"" + key + "\"");
    }
    
    public void testGetFollowsWithFile() {
        FileResource fr = new FileResource();
        String st = fr.asString();
        st = st.replace('\n', ' ');
        MarkovOne markov = new MarkovOne();
        markov.setTraining(st);
        String key = "he";
        ArrayList<String> follows = markov.getFollows(key);
        System.out.println("Letters that follow \"" + key + "\": " + follows);
        System.out.println("There are " + follows.size() + " letters that follow \"" + key + "\"");
    }

}
