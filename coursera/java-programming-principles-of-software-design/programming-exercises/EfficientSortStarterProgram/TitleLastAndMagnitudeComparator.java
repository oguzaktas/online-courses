
/**
 * Write a description of TitleAndDepthComparator here.
 * 
 * Oguz Aktas
 * @version 1.0
 */

import java.util.*;

public class TitleLastAndMagnitudeComparator implements Comparator<QuakeEntry> {
    
    public int compare(QuakeEntry q1, QuakeEntry q2) {
        String q1string = q1.getInfo().toString();
        String lastWord1 = q1string.substring(q1string.lastIndexOf(" ") + 1);
        String q2string = q2.getInfo().toString();
        String lastWord2 = q2string.substring(q2string.lastIndexOf(" ") + 1);
        
        if (lastWord1.compareTo(lastWord2) < 0) {
            return -1;
        } else if (lastWord1.compareTo(lastWord2) > 0) {
            return 1;
        } else {
            return Double.compare(q1.getMagnitude(), q2.getMagnitude());
        }
    }

}
