
/**
 * Write a description of DistanceFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */
public class DistanceFilter implements Filter {
    
    private Location location;
    private float maxDistance;
    private String name;
    
    public DistanceFilter(Location loc, float dist, String filterName) {
        location = loc;
        maxDistance = dist;
        name = filterName;
    }
    
    public Location getLocation() {
        return location;
    }
    
    public float getMaxDistance() {
        return maxDistance;
    }
    
    public String getName() {
        return name;
    }
    
    public void setLocation(Location loc) {
        location = loc;
    }
    
    public void setMaxDistance(float dist) {
        maxDistance = dist;
    }
    
    public boolean satisfies(QuakeEntry qe) {
        return qe.getLocation().distanceTo(location) / 1000.0 < maxDistance;
    }

}
