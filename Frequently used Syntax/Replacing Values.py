    obj_df["num_cylinders"].value_counts()

            four      159
            six        24
            five       11
            eight       5
            two         4
            twelve      1
            three       1
            Name: num_cylinders, dtype: int64

#If you review the replace documentation, you can see that it is a powerful command that has many options. For our uses, we are going to create a mapping dictionary that contains each column to process as well as a dictionary of the values to translate.

#Here is the complete dictionary for cleaning up the num_doors and num_cylinders columns:

    cleanup_nums = {"num_doors":     {"four": 4, "two": 2},
                    "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8, 
                    "two": 2, "twelve": 12, "three":3 }}

#To convert the columns to numbers using replace :

    obj_df.replace(cleanup_nums, inplace=True)
    obj_df.head()
