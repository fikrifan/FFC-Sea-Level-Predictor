import unittest
import sea_level_predictor
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")

    def test_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")

    def test_plot_data_points(self):
        # Retrieve the lines plotted
        lines = self.ax.get_lines()
        # There should be 2 lines of best fit + the scatter points (which are a Collection, not a Line2D usually, but sometimes handled differently depending on implementation)
        # scatter is usually a PathCollection. The lines are Line2D.
        # We expect 2 lines (red and green)
        self.assertEqual(len(lines), 2, "Expected two lines of best fit to be plotted.")
        
        # Check first line (1880-2050)
        # We check a point on the line to verify the slope/intercept
        # x = 2050. Using slope ~0.063 and intercept ~-119
        # y = 0.063 * 2050 - 119 = ~10.1
        
        # Line 0 data
        x_data_0 = lines[0].get_xdata()
        y_data_0 = lines[0].get_ydata()
        
        self.assertEqual(x_data_0[0], 1880, "Expected first line to start at year 1880")
        # 2050 index is 170 (2050 - 1880)
        self.assertEqual(x_data_0[-1], 2050, "Expected first line to end at year 2050")
        
    def test_plot_lines(self):
        lines = self.ax.get_lines()
        # Check slopes implicitly by checking end values
        # Line 1 (all data) prediction for 2050 should be around 10.17
        y_data_0 = lines[0].get_ydata()
        self.assertAlmostEqual(y_data_0[-1], 10.175, places=1, msg="Expected first line of best fit to predict ~10.17 inches for 2050")
        
        # Line 2 (2000+ data) prediction for 2050 should be around 15.38
        y_data_1 = lines[1].get_ydata()
        self.assertAlmostEqual(y_data_1[-1], 15.38, places=1, msg="Expected second line of best fit to predict ~15.38 inches for 2050")

if __name__ == "__main__":
    unittest.main()