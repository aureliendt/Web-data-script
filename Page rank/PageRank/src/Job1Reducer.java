/***
 * Class Job1Reducer
 * Job1 Reducer class
 * @author sgarouachi
 */

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Job1Reducer extends Reducer<Text, Text, Text, Text> {

	/**
	 * Job1 Reduce method (page, 1.0 \t outLinks)
	 * Remove redundant links & sort them Asc
	 */
	@Override
	public void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {
		// TODO if needed
		// Remove redundant outLinks
		
		// String outlinks = "";
		ArrayList<String> links = new ArrayList<String>();       
		Iterator<Text> iter = values.iterator();
		        while(iter.hasNext()){
		     	   Text t = iter.next();
		     	   String v = t.toString();  	   
		            //remove duplicate references.
		            if((!links.contains(v))){
		            	// outlinks += v; 
		            // outlinks+=',';
		            links.add(v);
		            }
		        }
	      
        //String links = "";
        //boolean first = true;
        //for (Text value : values) {
        	//	if (!first) 
        	//		links += "," ;
         //   if (!links.contains(value.toString()))
         //   		links +=  value.toString();
         //   first = false;
            
        //}
        
       // List<String> linkss = Arrays.asList(links.split(","));
        Collections.sort(links);
        String linksss = String.join(",", links);
        
        if (linksss.isEmpty()) {
        	context.write(key, new Text("1.0"));
        } else
        	context.write(key, new Text("1.0\t"+ linksss));
        	
        
        

		// Sort outLinks by Asc
		// Append default page rank + outLinks
		// throw new UnsupportedOperationException("Job1Reducer: reduce: Not implemented yet");
        
       
	}
}
