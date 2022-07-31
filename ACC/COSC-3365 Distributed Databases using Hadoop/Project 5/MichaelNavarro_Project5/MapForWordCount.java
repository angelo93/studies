import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//***************************************************************
//
//  Class:        MapperForWordCount
//
//  Method:       map
// 
//  Description:  This is the Mapper Class program for the
//                WordCount program using MapReduce
//
//  Parameters:   Method parameters: LongWritable, Text, and Context
//
//  Returns:      (key, value) pair => (NAME, 1)
//
//**************************************************************
public class MapForWordCount extends Mapper<LongWritable, Text, Text, IntWritable>
{
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
	{
		// Key=0, Value=john,lupa,john,frank,frank,john,...,frank,frank,lupa,steve

		String line = value.toString();
		//line=john,lupa,john,frank,frank,john,...,frank,frank,lupa,steve

        String[] words = line.split(",");
		// words = [john,lupa,john,frank,frank,john,...,frank,frank,lupa,steve]
		for (String word : words)
		{
			// Convert the word to upper case and assign it to outputKey
			Text outputKey = new Text(word.toUpperCase().trim()); 
			
			// create an outputValue and assign it a value of 1				
			IntWritable outputValue = new IntWritable(1);
			
			// Use Object of Context class to collect the (key,value) pairs
			// (JOHN, 1)
			// (LUPA, 1)
			context.write(outputKey, outputValue);  // Collect the (key,value) (JOHN, 1)
		}
	}
}