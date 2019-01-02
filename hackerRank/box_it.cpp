// SOLVED
#include<iostream>
using namespace std;


class Box {

  private:

      long long l;
      long long b;
      long long h;

  public:

    Box () {
      this->l = 0;
      this->b = 0;
      this->h = 0;
    }

    Box (int l, int b, int h) {
      this->l = l;
      this->b = b;
      this->h = h;
    }

    Box (const Box &obj) {
      this->l = obj.getLength();
      this->b = obj.getBreadth();
      this->h = obj.getHeight();
    }

    long long getLength () const {
      return this->l;
    }

    long long getBreadth () const {
      return this->b;
    }

    long long getHeight () const {
      return this->h;
    }

    long long CalculateVolume () {
      return (this->l * this->b * this->h);
    }

   friend bool operator<(Box &a, Box &b)  {
      if (a.getLength() < b.getLength()) {
        return true;
      } else if (a.getBreadth() < b.getBreadth() && a.getLength() == b.getLength()) {
        return true;
      } else if (a.getHeight() < b.getHeight() && a.getBreadth() == b.getBreadth() && b.getLength() == b.getLength()) {
        return true;
      }
      return false;
    }

    friend ostream &operator<<(ostream &out, const Box &b) {
      out<<b.getLength()<<" "<<b.getBreadth()<<" "<<b.getHeight();
      return out;
    }
};


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}


// INPUT

// 6
// 2 1039 3749 8473
// 4
// 3 1456 3836 283
// 3 729 3749 272
// 2 4839 283 273
// 4

// OUTPUT
// 1039 3749 8473
// 33004122803
// Greater
// Lesser
// 4839 283 273
// 373856301
