import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

//***************************************************************
//
//  Class:        Project6Reducer
//
//  Method:       reduce
// 
//  Description:  This is the Reducer Class program for the
//                Project 6 program using MapReduce
//
//  Parameters:   Method parameters: Text, Iterable<Text>, and Context
//
//  Returns:      Category City SuccessRate 
//
//**************************************************************
public class Project6Reducer extends Reducer<Text, Text, Text, Text>
{
	@Override
	public void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException
	{   
		// An object Implementing Iterable allows it to be iterated
	    // An iterable interface allows an object to be the target of
		// enhanced for loop(for-each loop). 
	    // Key=(city state), Value=[(clicks,sales),(clicks,sales)...(clicks,sales)]
	
		int numAdvertisements = 0;	// used as the total count for arithmetic
		double runningTotal = 0.0; 	// Total of clicks/sales for total iterations
		double successRate = 0.0;	// Success rate of all advertisements ((sales/clicks) *100)+Nth((sales/clicks) * 100) / N
		
		Iterator<Text> valuesIterator = values.iterator();
		while(valuesIterator.hasNext())
		{
			numAdvertisements += 1;
			
			// Convert our value pairs into a list
			String val = valuesIterator.next().toString();
			String [] vals = val.split(",");
			
			// Convert our numbers to doubles for arithmetic
	        double clicks = Double.parseDouble(vals[0]);
	        double sales  = Double.parseDouble(vals[1]);
	        
	        // Calculate the success rate for the current advertisement
	        double tmpSuccessRate = (sales/clicks) * 100;
	        
	        // Add to running total
	        runningTotal += tmpSuccessRate;
		}
		
		// This will cause an error if for some reason a key has no value, 
		// we will assume proper data cleaning has been done and we won't divide by 0
		successRate = runningTotal/numAdvertisements;
		
		// Convert our value pairs into a list
		String [] keys = key.toString().split(",");
		
		String cat = String.format("%-9s", keys[0]);
		String city = String.format("%-11s", keys[1]);
		
		String outputKey = (cat + " " + city);
		String outputVal = String.format("%.2f", successRate);
		
		context.write(new Text(outputKey), new Text(outputVal));
	}
}
