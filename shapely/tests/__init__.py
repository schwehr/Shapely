from unittest import TestSuite

import test_doctests, test_prepared, test_equality, test_geomseq, test_xy
import test_collection, test_emptiness, test_singularity, test_validation
import test_mapping, test_delegated, test_dlls, test_linear_referencing
import test_products_z, test_box, test_speedups, test_cga, test_getitem
import test_ndarrays, test_unary_union, test_pickle, test_affinity
import test_transform, test_styles, test_cascaded_union

def test_suite():
    suite = TestSuite()
    suite.addTest(test_doctests.test_suite())
    suite.addTest(test_prepared.test_suite())
    suite.addTest(test_emptiness.test_suite())
    suite.addTest(test_equality.test_suite())
    suite.addTest(test_geomseq.test_suite())
    suite.addTest(test_xy.test_suite())
    suite.addTest(test_collection.test_suite())
    suite.addTest(test_singularity.test_suite())
    suite.addTest(test_validation.test_suite())
    suite.addTest(test_mapping.test_suite())
    suite.addTest(test_delegated.test_suite())
    suite.addTest(test_dlls.test_suite())
    suite.addTest(test_linear_referencing.test_suite())
    suite.addTest(test_products_z.test_suite())
    suite.addTest(test_box.test_suite())
    suite.addTest(test_speedups.test_suite())
    suite.addTest(test_cga.test_suite())
    suite.addTest(test_getitem.test_suite())
    suite.addTest(test_ndarrays.test_suite())
    suite.addTest(test_cascaded_union.test_suite())
    suite.addTest(test_unary_union.test_suite())
    suite.addTest(test_pickle.test_suite())
    suite.addTest(test_affinity.test_suite())
    suite.addTest(test_transform.test_suite())
    suite.addTest(test_styles.test_suite())
    return suite
