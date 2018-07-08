/***
 * Class Job2Reducer
 * Job2 Reducer class
 * @author sgarouachi
 */

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Job2Reducer extends Reducer<Text, Text, Text, Text> {
	// Init dumping factor to 0.85
	private static final float damping = 0.85F;

	/**
	 * Job2 Reduce method Calculate the new page rank
	 */
	@Override
	public void reduce(Text page, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {
		// For each otherPage: 
        // - check control characters
        // - calculate pageRank share <rank> / count(<links>)
		String links = "";
        float sumShareOtherPageRanks = 0;
        	boolean Exist = false;
        for (Text value : values) {
        	 
            String content = value.toString();
            
            if (content.equals("!")) {
            			Exist=true;
            			continue;
            }
            else if (content.startsWith("|")) {
                // if this value contains node links append them to the 'links' string
                // for future use: this is needed to reconstruct the input for Job#2 mapper
                // in case of multiple iterations of it.
                links += "\t" + content.substring(1);
                continue;
            } else {
                
                String[] split = content.split("\\t");
                
                // extract tokens
                float pageRank = Float.parseFloat(split[1]);
                int totalLinks = Integer.parseInt(split[2]);
                
                // add the contribution of all the pages having an outlink pointing 
                // to the current node: we will add the DAMPING factor later when recomputing
                // the final pagerank value before submitting the result to the next job.
                sumShareOtherPageRanks += (pageRank / totalLinks);
            }

        }
        
        if(!Exist) return;
        float newRank = damping * sumShareOtherPageRanks + (1 - damping);
		// Write to output
		// (page, rank \t outLinks)
		context.write(page, new Text(String.format(java.util.Locale.US,"%.4f", newRank)  + links));

		// TODO if needed
		//throw new UnsupportedOperationException(
		//		"Job2Reducer: reduce: Not implemented yet");
	}
}
