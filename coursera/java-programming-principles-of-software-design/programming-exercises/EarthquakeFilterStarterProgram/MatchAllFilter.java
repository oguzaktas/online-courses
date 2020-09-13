
/**
 * Write a description of MatchAllFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */

import java.util.*;
import edu.duke.*;

public class MatchAllFilter implements Filter {
    
    private ArrayList<Filter> filters;
    private String name;
    
    public MatchAllFilter() {
        filters = new ArrayList<Filter>();
    }
    
    public String getName() {
        return name;
    }
    
    public void addFilter(Filter f) {
        filters.add(f);
    }
    
    public boolean satisfies(QuakeEntry qe) {
        for (Filter f : filters) {
            if (!f.satisfies(qe))
                return false;
        }
        return true;
    }

}
