import java.util.*;
import edu.duke.*;

public class EarthQuakeClient2 {
    public EarthQuakeClient2() {
        // TODO Auto-generated constructor stub
    }

    public ArrayList<QuakeEntry> filter(ArrayList<QuakeEntry> quakeData, Filter f) { 
        ArrayList<QuakeEntry> answer = new ArrayList<QuakeEntry>();
        for(QuakeEntry qe : quakeData) { 
            if (f.satisfies(qe)) { 
                answer.add(qe); 
            } 
        } 
        
        return answer;
    } 

    public void quakesWithFilter() { 
        EarthQuakeParser parser = new EarthQuakeParser(); 
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        // String source = "data/nov20quakedatasmall.atom";
        String source = "data/nov20quakedata.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);         
        System.out.println("read data for "+list.size()+" quakes");
        
        /*
        Filter f = new MinMagFilter(4.0); 
        ArrayList<QuakeEntry> m7  = filter(list, f); 
        for (QuakeEntry qe: m7) { 
            System.out.println(qe);
        }
        */
        
        /*
        Filter magnitudeFilter = new MagnitudeFilter(4.0, 5.0, "Magnitude"); 
        ArrayList<QuakeEntry> filteredByMagnitude = filter(list, magnitudeFilter);
        
        Filter depthFilter = new DepthFilter(-35000.0, -12000.0, "Depth");
        ArrayList<QuakeEntry> filteredByDepth = filter(filteredByMagnitude, depthFilter);
        
        for (QuakeEntry qe: filteredByDepth) { 
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredByDepth.size());
        */
        
        /*
        Location tokyo = new Location(35.42, 139.43);
        Filter distanceFilter = new DistanceFilter(tokyo, 10000);
        ArrayList<QuakeEntry> filteredByDistance = filter(list, distanceFilter);
        
        Filter phraseFilter = new PhraseFilter("end", "Japan");
        ArrayList<QuakeEntry> filteredByPhrase = filter(filteredByDistance, phraseFilter);
        
        for (QuakeEntry qe : filteredByPhrase) {
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " 
                            + filteredByPhrase.size());
        */
       
        /*
        Filter depthFilter = new DepthFilter(-4000.0, -2000.0, "Depth");
        ArrayList<QuakeEntry> filteredByDepth = filter(list, depthFilter);
        
        for (QuakeEntry qe: filteredByDepth) { 
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredByDepth.size());
        */
        
        /*
        Filter phraseFilter = new PhraseFilter("any", "Can  ", "Phrase");
        ArrayList<QuakeEntry> filteredByPhrase = filter(list, phraseFilter);
        
        for (QuakeEntry qe: filteredByPhrase) { 
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredByPhrase.size());
        */
       
        Location denver = new Location(39.7392, -104.9903);
        Filter distanceFilter = new DistanceFilter(denver, 1000, "Distance");
        ArrayList<QuakeEntry> filteredByDistance = filter(list, distanceFilter);
        
        Filter phraseFilter = new PhraseFilter("end", "a", "Phrase");
        ArrayList<QuakeEntry> filteredByPhrase = filter(filteredByDistance, phraseFilter);
        
        for (QuakeEntry qe : filteredByPhrase) {
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredByPhrase.size());
        
    }

    public void createCSV() {
        EarthQuakeParser parser = new EarthQuakeParser();
        //String source = "../data/nov20quakedata.atom";
        String source = "data/nov20quakedatasmall.atom";
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);
        dumpCSV(list);
        System.out.println("# quakes read: "+list.size());
    }

    public void dumpCSV(ArrayList<QuakeEntry> list) {
        System.out.println("Latitude,Longitude,Magnitude,Info");
        for(QuakeEntry qe : list){
            System.out.printf("%4.2f,%4.2f,%4.2f,%s\n",
                qe.getLocation().getLatitude(),
                qe.getLocation().getLongitude(),
                qe.getMagnitude(),
                qe.getInfo());
        }
    }
    
    public void testMatchAllFilter() {
        EarthQuakeParser parser = new EarthQuakeParser(); 
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        //String source = "data/nov20quakedatasmall.atom";
        String source = "data/nov20quakedata.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);         
        System.out.println("read data for "+list.size()+" quakes");
        
        MatchAllFilter maf = new MatchAllFilter();
        maf.addFilter(new MagnitudeFilter(1.0, 4.0, "Magnitude"));
        maf.addFilter(new DepthFilter(-180000.0, -30000.0, "Depth"));
        maf.addFilter(new PhraseFilter("any", "o", "Phrase"));
        
        ArrayList<QuakeEntry> filteredQuakes = filter(list, maf);
        for (QuakeEntry qe : filteredQuakes) {
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredQuakes.size());
        System.out.println("Filters used are: " + maf.getName());
    }
    
    public void testMatchAllFilter2() {
        EarthQuakeParser parser = new EarthQuakeParser(); 
        //String source = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom";
        //String source = "data/nov20quakedatasmall.atom";
        String source = "data/nov20quakedata.atom";
        ArrayList<QuakeEntry> list  = parser.read(source);         
        System.out.println("read data for "+list.size()+" quakes");
        
        MatchAllFilter maf = new MatchAllFilter();
        maf.addFilter(new MagnitudeFilter(0.0, 5.0, "Magnitude"));
        Location billund = new Location(55.7308, 9.1153);
        Filter distanceFilter = new DistanceFilter(billund, 3000, "Distance");
        maf.addFilter(new PhraseFilter("any", "e", "Phrase"));
        
        ArrayList<QuakeEntry> filteredQuakes = filter(list, maf);
        for (QuakeEntry qe : filteredQuakes) {
            System.out.println(qe);
        }
        
        System.out.println("Number of earthquakes that match the criteria: " + filteredQuakes.size());
        System.out.println("Filters used are: " + maf.getName());
    }

}
