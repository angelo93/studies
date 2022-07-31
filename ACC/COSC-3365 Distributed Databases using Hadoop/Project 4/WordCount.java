//***************************************************************
//
//  Developer:     <Your full name>
//
//  Project #:     Four
//
//  File Name:     WordCount.java
//
//  Course:        COSC 3365 – Distributed Databases Using Hadoop 
//
//  Due Date:      <Due Date>
//
//  Instructor:    Prof. Fred Kumi 
//
//  Description:   <An explanation of what the program is
//                 designed to do>
//
//***************************************************************

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCount
{
	//***************************************************************
    //
    //  Method:       main
    // 
    //  Description:  The main method of the program
    //
    //  Parameters:   String array
    //
    //  Returns:      N/A 
    //
    //**************************************************************
	public static void main(String[] args) throws Exception
	{
		if (args.length != 2)
		{
			System.err.println("Usage: WordCount <input path> <output path>");
			System.exit(-1);
		}
		
		// The Driver class instantiates a Job object. The Job object creates
		// and stores the configuration options for the Job, including the
		// classes to be used as the Mapper and Reducer, input and output
		// directories, and other options, such as the Job name that will
		// display in the YARN ResourceManager UI.
		Configuration conf = new Configuration();
		
		String[] files = new GenericOptionsParser(conf, args).getRemainingArgs();

        // Job name that will be displayed in the YARN ResourceManager UI.
		Job job = Job.getInstance(conf, "wordcount");
		
		// The Driver class
		job.setJarByClass(WordCount.class);
		
		//Set input and output locations
		Path input = new Path(files[0]);
		Path output = new Path(files[1]);
		FileInputFormat.addInputPath(job, input);
		FileOutputFormat.setOutputPath(job, output);
				
        // Or
		// FileInputFormat.addInputPath(job, new Path(args[0]));
		// FileOutputFormat.setOutputPath(job, new Path(args[1]));

		//Set Input and Output formats
	    job.setInputFormatClass(TextInputFormat.class);
	    job.setOutputFormatClass(TextOutputFormat.class);

		//Set Mapper and Reduce classes
		job.setMapperClass(MapperForWordCount.class);
		job.setReducerClass(ReducerForWordCount.class);
		
		//Output types
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
        // Submit Job
		System.exit(job.waitForCompletion(true) ? 0 : 1);
		
		// Or written expanded
		// boolean status = job.waitForCompletion(true);
		// if (status)
		//    System.exit(0);
		// else
		//    System.exit(1);
	}

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
    //  Returns:      N/A 
    //
    //**************************************************************
	public static class MapperForWordCount extends Mapper<LongWritable, Text, Text, IntWritable>
	{
		@Override
		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
		{// Key=0, Value=john,lupa,john,frank,frank,john,...,frank,frank,lupa,steve

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
	
	//***************************************************************
    //
    //  Class:        ReducerForWordCount
	//
	//  Method:       reduce
    // 
    //  Description:  This is the Reducer Class program for the
    //                WordCount program using MapReduce
    //
    //  Parameters:   Method parameters: Test, Iterable<IntWritable>, and Context
    //
    //  Returns:      N/A 
    //
    //**************************************************************
	public static class ReducerForWordCount extends Reducer<Text, IntWritable, Text, IntWritable>
	{
		@Override
		public void reduce(Text word, Iterable<IntWritable> values, Context context)
				throws IOException, InterruptedException
		{   // An object Implementing Iterable allows it to be iterated
		    // An iterable interface allows an object to be the target of
			// enhanced for loop(for-each loop). 
		    // Key=JOHN, Value=[1,1,1,1,1,1,...,1]
		
			int sum = 0;
			for (IntWritable value : values)
			{
				sum += value.get();
			}
			context.write(word, new IntWritable(sum));
		}
	}
}
