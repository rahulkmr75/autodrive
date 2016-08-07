#include <iostream>
#ifndef NULL
#define NULL 0L
#endif
#include "tree.h"
#ifndef TREE_2_H
#define TREE_2_H
class tree2{
public:
	point data;
	int level,nchild;
	point pardata;
	tree2 *child[8];
	tree2(point p){
		data.setval(p.x,p.y,p.z);
	}
	tree2(int x=0,int y=0,int z=0){
		data.setval(x,y,z);
	}
	void addchild(point p){
		child[nchild++]=new tree2(p);
		pardata.setval(data.x,data.y);
	}
};
#endif
