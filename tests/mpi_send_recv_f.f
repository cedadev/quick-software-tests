      program main
      include 'mpif.h' 

      integer ierr, world_rank, world_size, source, destination, number
      integer num1, target
      num1 = 100
      
      call mpi_init( ierr )

      call mpi_comm_rank( MPI_COMM_WORLD, world_rank, ierr ) 

      call mpi_comm_size( MPI_COMM_WORLD, world_size, ierr ) 
      
      if (world_size < 2) then
        print *,'World size must be greater than 1'
        call mpi_abort(MPI_COMM_WORLD, ierr)
      endif

      if (world_rank > 0) then
        source = world_rank - 1
        call mpi_recv( number, 1, MPI_INT, source, 0, MPI_COMM_WORLD,
     $       MPI_STATUS_IGNORE, ierr )
        
        print *,'Process ', world_rank, 'received number', number,
     $       'from process', source
      else
        number = num1
        print *,'Process ', world_rank, 'initialised number = ', number
      endif
      
      number = number + world_rank
      
      if (world_rank < world_size - 1) then
        
        destination = world_rank + 1;
        
        call mpi_send(number, 1, MPI_INT, destination, 0, 
     $       MPI_COMM_WORLD, ierr)
        
        print *,'Process ', world_rank, 'sent number', number,
     $       'to process', destination
        
      else
        target = 100 + world_rank * (world_rank + 1) / 2
         
        print *,'Process ', world_rank, 'Final answer', number,
     $       'should be', target

        if (number == target) then
          print *, 'SUCCESS FOR NPROC = ', world_size
        else
          print *, 'FAILURE'
        endif
         
      endif

      call mpi_finalize(ierr)

      end
