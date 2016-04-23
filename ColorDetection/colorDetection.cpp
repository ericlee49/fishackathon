#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "colordetector.h"
int main()
{z
        // Create image processor object
        ColorDetector cdetect;
        // Read input image
        cv::Mat image= cv::imread("goldfish.png");
        if (!image.data)
                return 0;
   // set input parameters
        cdetect.setTargetColor(23,23,242); // start with yellow
   // Read image, process it and display the result
        cv::namedWindow("result");
        cv::namedWindow("original");
        cv::imshow("result",cdetect.process(image));
        cv::imshow("original", image);
        cv::waitKey();
        return 0;
}
