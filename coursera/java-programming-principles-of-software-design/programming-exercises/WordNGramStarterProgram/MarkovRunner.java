
/**
 * Write a description of interface IMarkovModel here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */

import edu.duke.*;

public class MarkovRunner {
    public void runModel(IMarkovModel markov, String text, int size){ 
        markov.setTraining(text); 
        System.out.println("running with " + markov); 
        for(int k=0; k < 3; k++){ 
            String st = markov.getRandomText(size); 
            printOut(st); 
        } 
    } 

    public void runModel(IMarkovModel markov, String text, int size, int seed){ 
        markov.setTraining(text); 
        markov.setRandom(seed);
        System.out.println("running with " + markov); 
        for(int k=0; k < 3; k++){ 
            String st = markov.getRandomText(size); 
            printOut(st); 
        } 
    } 

    public void runMarkov() { 
        FileResource fr = new FileResource(); 
        String st = fr.asString(); 
        st = st.replace('\n', ' '); 
        //MarkovWordOne markovWord = new MarkovWordOne(); 
        MarkovWordTwo markovWord = new MarkovWordTwo();
        runModel(markovWord, st, 500, 832); 
    }
    
    public void runMarkovOne() { 
        FileResource fr = new FileResource(); 
        String st = fr.asString(); 
        st = st.replace('\n', ' '); 
        
        MarkovWordOne markovWord = new MarkovWordOne(); 
        runModel(markovWord, st, 120, 139); 
    } 
    
    public void runMarkovTwo() { 
        FileResource fr = new FileResource(); 
        String st = fr.asString(); 
        st = st.replace('\n', ' '); 
        
        MarkovWordTwo markovWord = new MarkovWordTwo(); 
        runModel(markovWord, st, 120, 832); 
    }

    private void printOut(String s){
        String[] words = s.split("\\s+");
        int psize = 0;
        System.out.println("----------------------------------");
        for(int k=0; k < words.length; k++){
            System.out.print(words[k]+ " ");
            psize += words[k].length() + 1;
            if (psize > 60) {
                System.out.println(); 
                psize = 0;
            } 
        } 
        System.out.println("\n----------------------------------");
    } 

}
