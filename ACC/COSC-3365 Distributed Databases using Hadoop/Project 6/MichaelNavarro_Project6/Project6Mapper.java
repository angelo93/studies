import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//***************************************************************
//
//  Class:        Project6Mapper
//
//  Method:       map
// 
//  Description:  This is the Mapper Class program for the
//                Project 6 using MapReduce
//
//  Parameters:   Method parameters: LongWritable, Text, and Context
//
//  Returns:      (key, value) pair => ("cat city", "clicks,sales")
//
//**************************************************************
public class Project6Mapper extends Mapper<LongWritable, Text, Text, Text>
{
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
	{
		// Key=0, Value=FKLY490998LB,2020-01-29 06:12:17,Austin,Ecommerce,39,13,25-35

		String line = value.toString();
		// line = FKLY490998LB,2020-01-29 06:12:17,Austin,Ecommerce,39,13,25-35

        String[] words = line.split(",");
		// words = [FKLY490998LB,2020-01-29 06:12:17,Austin,Ecommerce,39,13,25-35]
        
        Text city = new Text(words[2]);
        // city = Austin
        
        Text category = new Text(words[3]);
        // category = Ecommerce
        
		// Concatenate city and category to make a unique key for mapping
		Text outputKey = new Text(category + "," + city); 
		
		Text outputValue = new Text(words[4] + "," + words[5]);
		// outputValue = clicks,sales
		
		// Use Object of Context class to collect the (key,value) pairs
		// ("cat city", "clicks,sales")
		context.write(outputKey, outputValue);  // Collect the (key,value) ("Ecommerce Austin", "39,13")
	}
}