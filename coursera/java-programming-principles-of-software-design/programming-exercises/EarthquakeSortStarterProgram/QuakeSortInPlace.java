
/**
 * Write a description of class QuakeSortInPlace here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */

import java.util.*;
import edu.duke.*;

public class QuakeSortInPlace {
    public QuakeSortInPlace() {
        // TODO Auto-generated constructor stub
    }
   
    public int getSmallestMagnitude(ArrayList<QuakeEntry> quakes, int from) {
        int minIdx = from;
        for (int i=from+1; i< quakes.size(); i++) {
            if (quakes.get(i).getMagnitude() < quakes.get(minIdx).getMagnitude()) {
                minIdx = i;
            }
        }
        return minIdx;
    }
    
    public void sortByMagnitude(ArrayList<QuakeEntry> in) {
       for (int i=0; i< in.size(); i++) {
            int minIdx = getSmallestMagnitude(in,i);
            QuakeEntry qi = in.get(i);
            QuakeEntry qmin = in.get(minIdx);
            in.set(i,qmin);
            in.set(minIdx,qi);
        }
    }

    public void testSort() {
        EarthQuakeParser parser = new EarthQuakeParser(); 
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        //String source = "data/nov20quakedatasmall.atom";
        //String source = "data/nov20quakedata.atom";
        //String source = "data/earthquakeDataSampleSix2.atom";
        //String source = "data/earthquakeDataSampleSix1.atom";
        //String source = "data/earthQuakeDataDec6sample1.atom";
        //String source = "data/earthQuakeDataDec6sample2.atom";
        //String source = "data/earthQuakeDataWeekDec6sample1.atom";
        String source = "data/earthQuakeDataWeekDec6sample2.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);  
        
        /*
        System.out.println("read data for "+list.size()+" quakes");    
        sortByMagnitude(list);
        for (QuakeEntry qe: list) { 
            System.out.println(qe);
        }
        */
        
        /*
        System.out.println("read data for " + list.size() + " quakes");
        sortByMagnitudeWithBubbleSortWithCheck(list);
        for (QuakeEntry qe : list) {
            System.out.println(qe);
        }
        */
       
        System.out.println("read data for " + list.size() + " quakes");
        sortByMagnitudeWithBubbleSortWithCheck(list);
        
            
        /*
        System.out.println("read data for " + list.size() + " quakes");
        sortByMagnitudeWithBubbleSort(list);
        for (QuakeEntry qe : list) {
            System.out.println(qe);
        }
        */
        
        /*
        System.out.println("read data for " + list.size() + " quakes");
        sortByMagnitudeWithBubbleSortWithCheck(list);
        for (QuakeEntry qe : list) {
            System.out.println(qe);
        }
        */
        
        /*
        System.out.println("read data for " + list.size() + " quakes");
        sortByMagnitudeWithCheck(list);
        for (QuakeEntry qe : list) {
            System.out.println(qe);
        }
        */
    }
    
    public void createCSV() {
        EarthQuakeParser parser = new EarthQuakeParser();
        //String source = "data/nov20quakedata.atom";
        String source = "data/nov20quakedatasmall.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        dumpCSV(list);
        System.out.println("# quakes read: " + list.size());
    }
    
    public void dumpCSV(ArrayList<QuakeEntry> list) {
	System.out.println("Latitude,Longitude,Magnitude,Info");
	for(QuakeEntry qe : list){
	    System.out.printf("%4.2f,%4.2f,%4.2f,%s\n", 
	    qe.getLocation().getLatitude(),
	    qe.getLocation().getLongitude(),
	    qe.getMagnitude(), qe.getInfo());
	}
    }
	   
    public int getLargestDepth(ArrayList<QuakeEntry> quakeData, int from) {
        int maxIdx = from;
        for (int i = from + 1; i < quakeData.size(); i++) {
            if (quakeData.get(i).getDepth() > quakeData.get(maxIdx).getDepth()) {
                maxIdx = i;
            }
        }
        return maxIdx;
    }
    
    public void sortByLargestDepth(ArrayList<QuakeEntry> in) {
        for (int i = 0; i < 70; i++) {
            int maxIdx = getLargestDepth(in, i);
            QuakeEntry qi = in.get(i);
            QuakeEntry qmax = in.get(maxIdx);
            in.set(i, qmax);
            in.set(maxIdx, qi);
        }
    }
    
    public void onePassBubbleSort(ArrayList<QuakeEntry> quakeData, int numSorted) {
        for (int i = 1; i < quakeData.size() - numSorted; i++) {
            QuakeEntry first = quakeData.get(i-1);
            QuakeEntry second = quakeData.get(i);
            if (first.getMagnitude() > second.getMagnitude()) {
                quakeData.set(i, first);
                quakeData.set(i-1, second);
            }
        }
    }
    
    public void sortByMagnitudeWithBubbleSort(ArrayList<QuakeEntry> in) {
        int numSorted = 0;
        while (numSorted < in.size()) {
            onePassBubbleSort(in, numSorted);
            numSorted++;
        }
    }
    
    public boolean checkInSortedOrder(ArrayList<QuakeEntry> quakes) {
        for (int i = 1; i < quakes.size(); i++) {
            QuakeEntry first = quakes.get(i-1);
            QuakeEntry second = quakes.get(i);
            if (first.getMagnitude() > second.getMagnitude()) {
                return false;
            }
        }
        return true;
    }
    
    public void sortByMagnitudeWithBubbleSortWithCheck(ArrayList<QuakeEntry> in) {
        int numSorted = 0;
        while (numSorted < in.size()) {
            onePassBubbleSort(in, numSorted);
            numSorted++;
            if (checkInSortedOrder(in)) {
                break;
            }
        }
        System.out.println(numSorted + " passes were needed to sort the elements.");
    }
    
    public void sortByMagnitudeWithCheck(ArrayList<QuakeEntry> in) {
        int numSorted = 0;
        for (int i = 0; i < in.size(); i++) {
            if (checkInSortedOrder(in)) {
                break;
            }
            int minIdx = getSmallestMagnitude(in, i);
            QuakeEntry qi = in.get(i);
            QuakeEntry qmin = in.get(minIdx);
            in.set(i,qmin);
            in.set(minIdx,qi);
            numSorted++;
        }
        System.out.println(numSorted + " passes were needed to sort the elements.");
    }
    
}
