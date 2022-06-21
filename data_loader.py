import os
import pandas as pd
import numpy as np
import cv2



class Count_DataLoader():

    def __init__(self,csv_file,image_folder) -> None:
        self.csv_file = csv_file
        self.image_folder = image_folder
        df = pd.read_csv(self.csv_file)
        for index, row in df.iterrows():
            image_name = row['image']
            image_ = cv2.imread(os.path.join(self.image_folder,image_name))
            cv2.imshow("display",image_)
            cv2.waitKey(0)
            print(row['image'], row['class'], row['count'])
        print(df)








if __name__ == "__main__":

    csv_file = '/home/lahiru/Computer_Vision/Classification/counting_CNN/data/grocery_items/test_sample1/lables.csv'
    img_folder = '/home/lahiru/Computer_Vision/Classification/counting_CNN/data/grocery_items/test_sample1'
    #df = pd.read_csv(csv_file)
    count_data = Count_DataLoader(csv_file,img_folder)