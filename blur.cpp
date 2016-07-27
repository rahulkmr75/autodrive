#include "tree.h"
#include "tree2.h"
#include <cv.h>
#include <vector>
#include <highgui.h>
#include <iostream>
#include <opencv2/opencv.hpp>


using namespace cv;
//using namespace std;
void extend (tree2 &node,Mat &img){
	int i,j,t1=node.data.x,t2=node.data.y;
	for(i=0;i<2;i++){
		for (j=-1;j<2;j++){
			Scalar intensity=img.at<uchar>(t2,t1);
			if (intensity.val[0]>127)
				node.addchild(point(t2,t1));
		}
	}
}
void black(tree2 &root,Mat &img,int level){
	int i,j,t1,t2;
	t1=root.data.x;
	t2=root.data.y
	
		
}
void findpath(Mat &img,tree &root){
	int i,j,k;
	for(i=0;i<root.nchild;i++);
		//extend(root.child[i],img);
}
int main(int argc, char const *argv[])
{
	Mat img=imread("f1.jpg",CV_LOAD_IMAGE_GRAYSCALE);

	int r=img.rows,c=img.cols;	
	std::cout<<r<<c<<"\n";
	point src(480,299);
	point dst(115,228);

	int i,j,t1,t2;
	Scalar intensity;
	Mat img1=img.clone();
	
	//the root
	tree2 root(src);
	root.level=0;
	img.at<uchar>(src.y,src.x)=0;
	extend(root,img);
	black(root,img);

	namedWindow("Original",1);
	imshow("Original",img);
	waitKey(0);
	return 0;
}
