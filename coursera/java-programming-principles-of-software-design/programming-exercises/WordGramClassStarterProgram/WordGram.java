
public class WordGram {
    private String[] myWords;
    private int myHash;

    public WordGram(String[] source, int start, int size) {
        myWords = new String[size];
        System.arraycopy(source, start, myWords, 0, size);
    }

    public String wordAt(int index) {
        if (index < 0 || index >= myWords.length) {
            throw new IndexOutOfBoundsException("bad index in wordAt "+index);
        }
        return myWords[index];
    }

    public int length(){
        return myWords.length;
    }

    public String toString(){
        String ret = "";
        for (int i = 0; i < myWords.length; i++) {
            String str = myWords[i] + " ";
            ret += str;
        }
        return ret.trim();
    }

    public boolean equals(Object o) {
        WordGram other = (WordGram) o;
        if (this.length() != other.length()) {
            return false;
        }
        for (int i = 0; i < myWords.length; i++) {
            if (!myWords[i].equals(other.wordAt(i))) {
                return false;
            }
        }
        return true;
    }

    public WordGram shiftAdd(String word) { 
        String[] myWordsCopy = new String[this.length()];
        for (int i = 0; i < myWordsCopy.length - 1; i++) {
            myWordsCopy[i] = this.myWords[i+1];
        }
        myWordsCopy[myWordsCopy.length - 1] = word;
        // TODO: Complete this method
        WordGram out = new WordGram(myWordsCopy, 0, myWordsCopy.length);
        return out;
    }
    
    public int hashCode() {
        return this.toString().hashCode();
    }

}