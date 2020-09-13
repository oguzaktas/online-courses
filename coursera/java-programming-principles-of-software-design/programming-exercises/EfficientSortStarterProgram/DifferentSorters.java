
/**
 * Write a description of class DifferentSorters here.
 * 
 * @author Oguz Aktas
 * @version 1.0
 */

import java.util.*;

public class DifferentSorters {
    public void sortWithCompareTo() {
        EarthQuakeParser parser = new EarthQuakeParser();
        //String source = "data/nov20quakedata.atom";
        String source = "data/earthQuakeDataWeekDec6sample1.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        Collections.sort(list);
        /*
        int counter = 0;
        for(QuakeEntry qe: list) {
            System.out.println(counter + " : " + qe);
            counter++;
        }
        */
        System.out.println(list.get(600));

    }    

    public void sortByMagnitude() {
        EarthQuakeParser parser = new EarthQuakeParser();
        String source = "data/nov20quakedata.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        Collections.sort(list, new MagnitudeComparator());
        for(QuakeEntry qe: list) {
            System.out.println(qe);
        }

    }

    public void sortByDistance() {
        EarthQuakeParser parser = new EarthQuakeParser();
        String source = "data/nov20quakedata.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        // Location is Durham, NC
        Location where = new Location(35.9886, -78.9072);
        Collections.sort(list, new DistanceComparator(where));
        for(QuakeEntry qe: list) {
            System.out.println(qe);
        }

    }
    
    public void sortByTitleAndDepth() {
        EarthQuakeParser parser = new EarthQuakeParser();
        //String source = "data/nov20quakedata.atom";
        //String source = "data/earthQuakeDataDec6sample1.atom";
        //String source = "data/earthQuakeDataWeekDec6sample1.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        String source = "data/earthQuakeDataWeekDec6sample2.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        
        Collections.sort(list, new TitleAndDepthComparator());
        /*
        int counter = 0;
        for(QuakeEntry qe: list) {
            System.out.println(counter + " : " + qe);
            counter++;
        }
        */
        System.out.println(list.get(500));
    }
    
    public void sortByLastWordInTitleThenByMagnitude() {
        EarthQuakeParser parser = new EarthQuakeParser();
        //String source = "data/nov20quakedata.atom";
        //String source = "data/earthQuakeDataDec6sample2.atom";
        String source = "data/earthQuakeDataWeekDec6sample1.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        
        Collections.sort(list, new TitleLastAndMagnitudeComparator());
        /*
        int counter = 0;
        for(QuakeEntry qe: list) {
            System.out.println(counter + " : " + qe);
            counter++;
        }
        */
        System.out.println(list.get(500));
    }
    
}
