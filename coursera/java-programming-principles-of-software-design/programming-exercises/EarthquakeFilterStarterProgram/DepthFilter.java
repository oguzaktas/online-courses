
/**
 * Write a description of DepthFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */
public class DepthFilter implements Filter {
    
    private double depthMin;
    private double depthMax;
    private String name;
    
    public DepthFilter(double min, double max, String filterName) {
        depthMin = min;
        depthMax = max;
        name = filterName;
    }
    
    public double getDepthMin() {
        return depthMin;
    }
    
    public double getDepthMax() {
        return depthMax;
    }
    
    public String getName() {
        return name;
    }
    
    public void setDepthMin(double min) {
        depthMin = min;
    }
    
    public void setDepthMax(double max) {
        depthMax = max;
    }
    
    public boolean satisfies(QuakeEntry qe) {
        return qe.getDepth() >= depthMin && qe.getDepth() <= depthMax;
    }

}
