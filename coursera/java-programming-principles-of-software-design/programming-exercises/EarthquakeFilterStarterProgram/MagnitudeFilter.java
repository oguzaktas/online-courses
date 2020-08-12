
/**
 * Write a description of MagnitudeFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */
public class MagnitudeFilter implements Filter {
    
    private double magMin;
    private double magMax;
    private String name;
    
    public MagnitudeFilter(double min, double max, String filterName) {
        magMin = min;
        magMax = max;
        name = filterName;
    }
    
    public double getMagMin() {
        return magMin;
    }
    
    public double getMagMax() {
        return magMax;
    }
    
    public String getName() {
        return name;
    }
    
    public void setMagMin(double min) {
        magMin = min;
    }
    
    public void setMagMax(double max) {
        magMax = max;
    }
    
    public boolean satisfies(QuakeEntry qe) {
        return qe.getMagnitude() >= magMin && qe.getMagnitude() <= magMax;
    }
    

}
