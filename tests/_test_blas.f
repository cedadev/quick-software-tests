      program dot_main
      real x(10), y(10), sdot, res
      integer n, incx, incy, i
      external sdot
      n = 5
      incx = 2
      incy = 1
      do i = 1, 10
        x(i) = 2.0e0
        y(i) = 1.0e0
      end do
      res = sdot (n, x, incx, y, incy)
      print *, int(res)
      end
