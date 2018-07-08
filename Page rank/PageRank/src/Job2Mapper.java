/***
 * Class Job2Mapper
 * Job2 Mapper class
 * @author sgarouachi
 */

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Job2Mapper extends Mapper<LongWritable, Text, Text, Text> {

	/**
	 * Job2 Map method Generates 3 outputs: Mark existing page: (pageI, !) Used
	 * to calculate the new rank (rank pageI depends on the rank of the inLink):
	 * (pageI, inLink \t rank \t totalLink) Original links of the page for the
	 * reduce output: (pageI, |pageJ,pageK...)
	 */ 
	@Override
	public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException {
		
		int tIdx1 = value.find("\t");
        int tIdx2 = value.find("\t", tIdx1 + 1);
        
        // extract tokens from the current line
        String page = Text.decode(value.getBytes(), 0, tIdx1);
        String pageRank = Text.decode(value.getBytes(), 0, tIdx2  + 1);
       
        
        
        context.write(new Text(page), new Text("!"));
        
        if (tIdx2 == -1) return;
        
        String links = Text.decode(value.getBytes(), tIdx2 + 1, value.getLength() - (tIdx2 + 1));
        String[] allOtherPages = links.split(",");
        
        
        if (!links.equals("")) {
        
        for (String otherPage : allOtherPages) { 
            Text pageRankWithTotalLinks = new Text(pageRank + allOtherPages.length);
            context.write(new Text(otherPage), pageRankWithTotalLinks); 
        }
        List<String> sortedLinks = Arrays.asList(links.split(","));
        Collections.sort(sortedLinks);
       
        context.write(new Text(page), new Text("|" + String.join(",", sortedLinks)));
        }
        
        // put the original links so the reducer is able to produce the correct output
        
        
 
        
		//throw new UnsupportedOperationException("Job2Mapper: map: Not implemented yet");
	}
}
