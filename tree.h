#ifndef NULL
#define NULL 0L
#endif
#ifndef POINT_H
#define POINT_H
class point{
public:
	int x,y,z;
	point(int x=0,int y=0,int z=0){
		setval(x,y,z);
	}
	void setval(int x=0,int y=0,int z=0){
		this->x=x;
		this->y=y;
		this->z=z;
	}	
};
#endif
#ifndef TREE_H
#define TREE_H
class tree{
public:
	point data;
	point pardata;
	tree **child;
	int nchild;
	//initializes the class attributes
	tree(int x=0,int y=0,int z=0){
		data.setval(x,y,z);
		nchild=0;
	}
	tree(point p){
		data.setval(p.x,p.y,p.z);
	}
	//allocates enough space to accomodate n child pointers
	void makechild(int n){
		child=new tree *[n];
		int i=0;
		for (;i<n;)child[i++]=NULL;
		nchild=n;
	}
	void addchild(point p){
		int i=0;
		for (;i<nchild;i++){
			if(child[i]==NULL){
				child[i]=new tree(p);
				nchild++;
				pardata.setval(data.x,data.y);
			}
		}
	}//addchild
};
#endif
