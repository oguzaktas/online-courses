
/**
 * Write a description of PhraseFilter here.
 * 
 * @ Oguz Aktas
 * @ Version 1.0
 */
public class PhraseFilter implements Filter {
    
    private String type;
    private String phrase;
    private String name;
    
    public PhraseFilter(String t, String p, String filterName) {
        type = t;
        phrase = p;
        name = filterName;
    }
    
    public String getType() {
        return type;
    }
    
    public String getPhrase() {
        return phrase;
    }
    
    public String getName() {
        return name;
    }
    
    public void setType(String t) {
        type = t;
    }
    
    public void setPhrase(String p) {
        phrase = p;
    }
    
    public boolean satisfies(QuakeEntry qe) {
        if (type == "start") {
            return qe.getInfo().startsWith(phrase);
        } else if (type == "end") {
            return qe.getInfo().endsWith(phrase);
        } else if (type == "any") {
            return qe.getInfo().contains(phrase);
        }
        return false;
    }

}
