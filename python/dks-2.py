# import sys

# # Function to find out which of the unvisited node 
# # needs to be visited next
# def to_be_visited():
#   global visited_and_distance
#   v = -10
#   # Choosing the vertex with the minimum distance
#   for index in range(number_of_vertices):

#     if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
#         v = index
#   return v

# # Creating the graph as an adjacency matrix
# vertices = [[0, 1, 1, 0],
#             [0, 0, 1, 0],
#             [0, 0, 0, 1],
#             [0, 0, 0, 0]]
# edges =  [[0, 3, 4, 0],
#           [0, 0, 0.5, 0],
#           [0, 0, 0, 1],
#           [0, 0, 0, 0]]

# number_of_vertices = len(vertices[0])

# # The first element of the lists inside visited_and_distance 
# # denotes if the vertex has been visited.
# # The second element of the lists inside the visited_and_distance 
# # denotes the distance from the source.
# visited_and_distance = [[0, 0]]
# for i in range(number_of_vertices-1):
#   visited_and_distance.append([0, sys.maxsize])

# for vertex in range(number_of_vertices):
#   # Finding the next vertex to be visited.
#   to_visit = to_be_visited()
#   for neighbor_index in range(number_of_vertices):
#     # Calculating the new distance for all unvisited neighbours
#     # of the chosen vertex.
#     if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
#       new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
#       # Updating the distance of the neighbor if its current distance
#       # is greater than the distance that has just been calculated
#       if visited_and_distance[neighbor_index][1] > new_distance:
#         visited_and_distance[neighbor_index][1] = new_distance
#   # Visiting the vertex found earlier
#   visited_and_distance[to_visit][0] = 1

# i = 0 

# # Printing out the shortest distance from the source to each vertex       
# for distance in visited_and_distance:
#   print("The shortest distance of ",chr(ord('a') + i), " from the source vertex a is:",distance[1])
#   i = i + 1


# include<iostream>
# include<climits>     
# using namespace std;

# // this method returns a minimum distance for the 
# // vertex which is not included in Tset.
# int minimumDist(int dist[], bool Tset[]) 
# {
# 	int min=INT_MAX,index;
              
# 	for(int i=0;i<6;i++) 
# 	{
# 		if(Tset[i]==false && dist[i]<=min)      
# 		{
# 			min=dist[i];
# 			index=i;
# 		}
# 	}
# 	return index;
# }

# void Dijkstra(int graph[6][6],int src) // adjacency matrix used is 6x6
# {
# 	int dist[6]; // integer array to calculate minimum distance for each node.                            
# 	bool Tset[6];// boolean array to mark visted/unvisted for each node.
	
# 	// set the nodes with infinity distance
# 	// except for the initial node and mark
# 	// them unvisited.  
# 	for(int i = 0; i<6; i++)
# 	{
# 		dist[i] = INT_MAX;
# 		Tset[i] = false;	
# 	}
	
# 	dist[src] = 0;   // Source vertex distance is set to zero.             
	
# 	for(int i = 0; i<6; i++)                           
# 	{
# 		int m=minimumDist(dist,Tset); // vertex not yet included.
# 		Tset[m]=true;// m with minimum distance included in Tset.
# 		for(int i = 0; i<6; i++)                  
# 		{
# 			// Updating the minimum distance for the particular node.
# 			if(!Tset[i] && graph[m][i] && dist[m]!=INT_MAX && dist[m]+graph[m][i]<dist[i])
# 				dist[i]=dist[m]+graph[m][i];
# 		}
# 	}
# 	cout<<"Vertex\t\tDistance from source"<<endl;
# 	for(int i = 0; i<6; i++)                      
# 	{ //Printing
# 		char str=65+i; // Ascii values for pritning A,B,C..
# 		cout<<str<<"\t\t\t"<<dist[i]<<endl;
# 	}
# }

# int main()
# {
# 	int graph[6][6]={
# 		{0, 10, 20, 0, 0, 0},
# 		{10, 0, 0, 50, 10, 0},
# 		{20, 0, 0, 20, 33, 0},
# 		{0, 50, 20, 0, 20, 2},
# 		{0, 10, 33, 20, 0, 1},
# 		{0, 0, 0, 2, 1, 0}};
# 	Dijkstra(graph,0);
# 	return 0;	                        
# }