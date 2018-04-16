# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from unittest import main, TestCase
from matplotlib import pyplot as plt
from matplotlib import patches

Arrow = patches.Arrow
Arc = patches.Arc
Circle = patches.Circle
CirclePolygon = patches.CirclePolygon
Rectangle = patches.Rectangle
Wedge = patches.Wedge


class TestPlotAPI(TestCase):
    def test_arrow(self):
        ax = plt.gca()
        arrow = Arrow(0, 0, 10, 0, edgecolor='red', facecolor='g', hatch='+')
        arrow2 = Arrow(10, 0, 0, 10, edgecolor='red', facecolor='g', hatch='+')
        arrow3 = Arrow(10, 10, -10, 0, edgecolor='red', facecolor='g', hatch='+')
        arrow4 = Arrow(0, 10, 0, -10, edgecolor='red', facecolor='g', hatch='+')
        ax.add_patch(arrow)
        ax.add_patch(arrow2)
        ax.add_patch(arrow3)
        ax.add_patch(arrow4)
        ax.axis('equal')
        plt.show()

    def test_arc(self):
        ax = plt.gca()
        arc = Arc((0, 0), 1, 2, angle=45, theta1=0, theta2=270)
        ax.add_patch(arc)
        ax.axis('equal')
        plt.show()


    def test_circle(self):
        ax = plt.gca()
        circle = Circle((0, 0), radius=10, hatch='+')
        ax.add_patch(circle)
        ax.axis('equal')
        plt.show()


    def test_circlepolygon(self):
        ax = plt.gca()
        circlepolygon = CirclePolygon((0, 0), radius=10, resolution=8)
        ax.add_patch(circlepolygon)
        ax.axis('equal')
        plt.show()

    def test_wedge(self):
        ax = plt.gca()
        wedge = Wedge((0, 0), 5, 0, 120, width=2)
        ax.add_patch(wedge)
        ax.axis('equal')
        plt.show()




if __name__ == "__main__":
    main()
