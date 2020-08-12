
/**
 * IMarkovModel is an interface that is implemented in the AbstractMarkovModel class.
 * 
 * 
 * @ Oguz Aktas
 * @ Version: 1.0
 */

public interface IMarkovModel {
    public void setRandom(int seed);
    
    public void setTraining(String text);
    
    public String getRandomText(int setSize);
}
