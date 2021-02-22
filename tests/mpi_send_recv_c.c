/* adapted from example by Wes Kendall on www.mpitutorial.com */

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  MPI_Init(NULL, NULL);
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  int num1 = 100;
  
  // We are assuming at least 2 processes for this task
  if (world_size < 2) {
    fprintf(stderr, "World size must be greater than 1 for %s\n", argv[0]);
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  int number;
  if (world_rank > 0) {

    int source;
    source = world_rank - 1;

    MPI_Recv(
      /* data         = */ &number, 
      /* count        = */ 1, 
      /* datatype     = */ MPI_INT, 
      /* source       = */ source, 
      /* tag          = */ 0, 
      /* communicator = */ MPI_COMM_WORLD, 
      /* status       = */ MPI_STATUS_IGNORE);

    printf("Process %d received number %d from process %d\n", world_rank, number, source);
  }
  else {
    number = num1;
    printf("Process %d initialised number = %d\n", world_rank, number);
  }

  number += world_rank;

  if (world_rank < world_size - 1) {

    int destination;
    destination = world_rank + 1;

    MPI_Send(
      /* data         = */ &number, 
      /* count        = */ 1, 
      /* datatype     = */ MPI_INT, 
      /* destination  = */ destination, 
      /* tag          = */ 0, 
      /* communicator = */ MPI_COMM_WORLD);

    printf("Process %d sent number %d to process %d\n", world_rank, number, destination);
  } else {
    int target = num1 + world_rank * (world_rank + 1) / 2;

    printf("Process %d Final answer: %d, should be %d\n", world_rank, number, 100 + world_rank * (world_rank + 1) / 2);

    if (number == target)
      printf("SUCCESS FOR NPROC = %d\n", world_size);
    else
      puts("FAILURE");
  }

  MPI_Finalize();
}
