
/**
 * Write a description of interface IMarkovModel here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */

public interface IMarkovModel {
    public void setTraining(String text);
    
    public void setRandom(int seed);
    
    public String getRandomText(int numChars);

}
