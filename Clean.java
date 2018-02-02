import java.io.IOException;

/**
 * Created by Zheng Xin on 7/11/2017.
 */
public class Clean {

    static String numRegex = "[0-9]+";
    static String alphaRegex = "[a-zA-Z]+";
    static String NARegex = "[a-zA-Z0-9]+";
    static String urlRegex1 = "^(http|https|ftp|file)://.*";
    static String urlRegex2 = ".*[/]*.*(.html)";
    static String pathRegex = ".*[:\\\\]+.*[>]*.*";
    static String fileRegex = "[.|\\w]*/.*[/]*.*";
    static String ipRegex = "\\W[0-9]+[.]+[0-9]+[.]+[0-9]+[.]+[0-9]+\\W";
    static String hourRegex = "[0-9]+[:]+[0-9]+[:]+[0-9]+.*";
    static String timeRegex = ".*[0-9]+(/|-|.)+[0-9]+(/|-|.)+[0-9]+";

    public static void WordToC(String[] word) throws IOException {
        for(int j = 0; j < word.length; j++){
            word[j]=word[j].trim();
            if (word[j].endsWith(",") || word[j].endsWith(".")
                    ||word[j].endsWith(";") || word[j].endsWith(":")
                    ||word[j].endsWith("?") || word[j].endsWith("!")
                    || word[j].endsWith(")") || word[j].endsWith("'")
                    || word[j].endsWith("\"") || word[j].endsWith(">")
                    || word[j].endsWith("&") || word[j].endsWith("-")) {
                word[j] = word[j].substring(0, word[j].length()-1);
            }
            if(word[j].startsWith(",") || word[j].startsWith(".")
                    ||word[j].startsWith(";") || word[j].startsWith(":")
                    ||word[j].startsWith("?") || word[j].startsWith("!")
                    || word[j].startsWith("(")|| word[j].startsWith("'")
                    || word[j].startsWith("\"") || word[j].startsWith("<")
                    || word[j].startsWith("&") || word[j].startsWith("-")){
                word[j] = word[j].substring(1, word[j].length());
            }
            if(word[j].matches(urlRegex1) || word[j].matches(urlRegex2)
                    || word[j].startsWith(urlRegex1) || word[j].endsWith(urlRegex1)){
                word[j] = "";
            }

            if(word[j].matches("\\W")){
                word[j] = "";
            }

            if(word[j].matches(".*[^a-zA-Z0-9#@,_.]+.*")){
                word[j] = "";
            }

            if(word[j].matches("[a-z]+(,)[a-z]+")){
                String[] sub = word[j].split(",");
                word[j] = "";
                for(String key: sub){
                    word[j] += key + " ";
                }
                word[j] = word[j].trim();
            }

            if(word[j].matches("[a-z]+[.][a-z]+")){
                String[] sub = word[j].split(".");
                word[j] = "";
                for(String key: sub){
                    word[j] += key + " ";
                }
                word[j] = word[j].trim();
            }

            if (word[j].endsWith(",") || word[j].endsWith(".")
                    ||word[j].endsWith(";") || word[j].endsWith(":")
                    ||word[j].endsWith("?") || word[j].endsWith("!")
                    || word[j].endsWith(")") || word[j].endsWith("'")
                    || word[j].endsWith("\"") || word[j].endsWith(">")
                    || word[j].endsWith("&") || word[j].endsWith("-")) {
                word[j] = word[j].substring(0, word[j].length()-1);
            }

            if(word[j].startsWith(",") || word[j].startsWith(".")
                    ||word[j].startsWith(";") || word[j].startsWith(":")
                    ||word[j].startsWith("?") || word[j].startsWith("!")
                    || word[j].startsWith("(")|| word[j].startsWith("'")
                    || word[j].startsWith("\"") || word[j].startsWith("<")
                    || word[j].startsWith("&") || word[j].startsWith("-")){
                word[j] = word[j].substring(1, word[j].length());
            }

            if(word[j].equals("RT") || word[j].equals("rt")|| word[j].equals("amp")
                    || word[j].equals("gt") ){
                word[j]="";
            }

            if(word[j].matches("_")){
                word[j] = "";
            }
        }
    }

    public static String clean(String text) throws Exception {
        text = text.toLowerCase();
        text = text.replaceAll("\\*", " ");
        text = text.replaceAll("\\(", " ");
        text = text.replaceAll("\\)", " ");
        text = text.replaceAll("\\[", " ");
        text = text.replaceAll("\\\\", " ");
        text = text.replaceAll("]", " ");
        text = text.replaceAll("<", " ");
        text = text.replaceAll(">", " ");
        text = text.replaceAll("!", " ");
//        text = text.replaceAll("#", " ");
        text = text.replaceAll("-", " ");
        text = text.replaceAll("$", " ");
        text = text.replaceAll("_{2,}", " ");
        text = text.replaceAll("={2,}", " ");
        text = text.replaceAll("-{2,}", " ");
        text = text.replaceAll("~{2,}", " ");
        text = text.replaceAll("\\.{2,}", " ");
        text = text.replaceAll("\\?{2,}", " ");
//        text = text.replaceAll("\\\"", " ");
        text = text.replaceAll("\"", " ");
        String[] word = text.split("\\s+");
        WordToC(word);
        String text_clean = "";
        for (int i = 0; i < word.length; i++) {
            if (!word[i].isEmpty()) {
                word[i] = word[i].replaceAll("[^a-zA-Z0-9@#,_.]+", " ");
                text_clean += word[i] + " ";
            }
        }
        text_clean = text_clean.trim();
        return text_clean;
    }
}
