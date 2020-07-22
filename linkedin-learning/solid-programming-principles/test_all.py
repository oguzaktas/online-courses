"""S.O.L.I.D Design.

Comprehensive test of the modules.

Python 3.4 or later is required.

Note that this must be in the parent folder of the
ch01, ch02, ch03, ch04, ch05, ch06, and ch07 folders.

To run any module individually, be sure that
the ``PYTHONPATH`` environment variable points to this parent folder.

"""

import unittest
import doctest

import ch_01_02_introduction

import ch_02_isp
import ch_02_01_segregate_example_classes
import ch_02_02_isp_applied
import ch_02_03_wrap_extend_decision
import ch_02_04_extend_alternatives

import ch_03_lsp
import ch_03_01_introduction_liskov_substitution
import ch_03_02_interface_variations
import ch_03_03_substitution_applied
import ch_03_04_default_values_for_parameters
import ch_03_05_avoiding_isinstance

import ch_04_ocp
import ch_04_01_introduction
import ch_04_03_open_closed_inheritance
import ch_04_04_ocp_extension_techniques

import ch_05_dip
import ch_05_01_introduction
import ch_05_02_dependency_injection
import ch_05_03_testing_consequences

import ch_06_srp
import ch_06_01_introduction
import ch_06_02_high_cohesion_and_indirection

import ch_07_02_test_driven_design

modules = (ch_01_02_introduction,
           ch_02_isp, ch_02_01_segregate_example_classes, ch_02_02_isp_applied, ch_02_03_wrap_extend_decision, ch_02_04_extend_alternatives,
           ch_03_lsp, ch_03_01_introduction_liskov_substitution, ch_03_02_interface_variations, ch_03_03_substitution_applied, ch_03_04_default_values_for_parameters, ch_03_05_avoiding_isinstance,
           ch_04_ocp, ch_04_01_introduction, ch_04_03_open_closed_inheritance, ch_04_04_ocp_extension_techniques,
           ch_05_dip, ch_05_01_introduction, ch_05_02_dependency_injection, ch_05_03_testing_consequences,
           ch_06_srp, ch_06_01_introduction, ch_06_02_high_cohesion_and_indirection,
           ch_07_02_test_driven_design,
          )

def suite():
    """Build a suite from doctest and unittest in each module.
    """
    doctest_suite = unittest.TestSuite(
        [doctest.DocTestSuite(m) for m in modules],
    )
    unittest_suite = unittest.TestSuite(
        [unittest.defaultTestLoader.loadTestsFromModule(m) for m in modules],
    )
    return unittest.TestSuite([doctest_suite, unittest_suite])

if __name__ == "__main__":
    runner= unittest.TextTestRunner()
    runner.run(suite())
