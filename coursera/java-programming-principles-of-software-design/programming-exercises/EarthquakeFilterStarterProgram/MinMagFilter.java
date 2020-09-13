
/**
 * Write a description of MinMagFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */
public class MinMagFilter implements Filter
{
    private double magMin; 
    private String name;
    
    public MinMagFilter(double min, String filterName) { 
        magMin = min;
        name = filterName;
    }
    
    public String getName() {
        return name;
    }

    public boolean satisfies(QuakeEntry qe) { 
        return qe.getMagnitude() >= magMin; 
    } 

}
