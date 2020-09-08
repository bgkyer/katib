# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1beta1-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1_unstructured_unstructured import V1UnstructuredUnstructured  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_metrics_collector_spec import V1beta1MetricsCollectorSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_objective_spec import V1beta1ObjectiveSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_parameter_assignment import V1beta1ParameterAssignment  # noqa: F401,E501


class V1beta1TrialSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'failure_condition': 'str',
        'metrics_collector': 'V1beta1MetricsCollectorSpec',
        'objective': 'V1beta1ObjectiveSpec',
        'parameter_assignments': 'list[V1beta1ParameterAssignment]',
        'primary_container_name': 'str',
        'primary_pod_labels': 'dict(str, str)',
        'retain_run': 'bool',
        'run_spec': 'V1UnstructuredUnstructured',
        'success_condition': 'str'
    }

    attribute_map = {
        'failure_condition': 'failureCondition',
        'metrics_collector': 'metricsCollector',
        'objective': 'objective',
        'parameter_assignments': 'parameterAssignments',
        'primary_container_name': 'primaryContainerName',
        'primary_pod_labels': 'primaryPodLabels',
        'retain_run': 'retainRun',
        'run_spec': 'runSpec',
        'success_condition': 'successCondition'
    }

    def __init__(self, failure_condition=None, metrics_collector=None, objective=None, parameter_assignments=None, primary_container_name=None, primary_pod_labels=None, retain_run=None, run_spec=None, success_condition=None):  # noqa: E501
        """V1beta1TrialSpec - a model defined in Swagger"""  # noqa: E501

        self._failure_condition = None
        self._metrics_collector = None
        self._objective = None
        self._parameter_assignments = None
        self._primary_container_name = None
        self._primary_pod_labels = None
        self._retain_run = None
        self._run_spec = None
        self._success_condition = None
        self.discriminator = None

        if failure_condition is not None:
            self.failure_condition = failure_condition
        if metrics_collector is not None:
            self.metrics_collector = metrics_collector
        if objective is not None:
            self.objective = objective
        self.parameter_assignments = parameter_assignments
        if primary_container_name is not None:
            self.primary_container_name = primary_container_name
        if primary_pod_labels is not None:
            self.primary_pod_labels = primary_pod_labels
        if retain_run is not None:
            self.retain_run = retain_run
        if run_spec is not None:
            self.run_spec = run_spec
        if success_condition is not None:
            self.success_condition = success_condition

    @property
    def failure_condition(self):
        """Gets the failure_condition of this V1beta1TrialSpec.  # noqa: E501

        Condition when trial custom resource is failed. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Failed\")#|#(status==\"True\")#  # noqa: E501

        :return: The failure_condition of this V1beta1TrialSpec.  # noqa: E501
        :rtype: str
        """
        return self._failure_condition

    @failure_condition.setter
    def failure_condition(self, failure_condition):
        """Sets the failure_condition of this V1beta1TrialSpec.

        Condition when trial custom resource is failed. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Failed\")#|#(status==\"True\")#  # noqa: E501

        :param failure_condition: The failure_condition of this V1beta1TrialSpec.  # noqa: E501
        :type: str
        """

        self._failure_condition = failure_condition

    @property
    def metrics_collector(self):
        """Gets the metrics_collector of this V1beta1TrialSpec.  # noqa: E501

        Describes how metrics will be collected  # noqa: E501

        :return: The metrics_collector of this V1beta1TrialSpec.  # noqa: E501
        :rtype: V1beta1MetricsCollectorSpec
        """
        return self._metrics_collector

    @metrics_collector.setter
    def metrics_collector(self, metrics_collector):
        """Sets the metrics_collector of this V1beta1TrialSpec.

        Describes how metrics will be collected  # noqa: E501

        :param metrics_collector: The metrics_collector of this V1beta1TrialSpec.  # noqa: E501
        :type: V1beta1MetricsCollectorSpec
        """

        self._metrics_collector = metrics_collector

    @property
    def objective(self):
        """Gets the objective of this V1beta1TrialSpec.  # noqa: E501

        Describes the objective of the experiment.  # noqa: E501

        :return: The objective of this V1beta1TrialSpec.  # noqa: E501
        :rtype: V1beta1ObjectiveSpec
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this V1beta1TrialSpec.

        Describes the objective of the experiment.  # noqa: E501

        :param objective: The objective of this V1beta1TrialSpec.  # noqa: E501
        :type: V1beta1ObjectiveSpec
        """

        self._objective = objective

    @property
    def parameter_assignments(self):
        """Gets the parameter_assignments of this V1beta1TrialSpec.  # noqa: E501

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :return: The parameter_assignments of this V1beta1TrialSpec.  # noqa: E501
        :rtype: list[V1beta1ParameterAssignment]
        """
        return self._parameter_assignments

    @parameter_assignments.setter
    def parameter_assignments(self, parameter_assignments):
        """Sets the parameter_assignments of this V1beta1TrialSpec.

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :param parameter_assignments: The parameter_assignments of this V1beta1TrialSpec.  # noqa: E501
        :type: list[V1beta1ParameterAssignment]
        """
        if parameter_assignments is None:
            raise ValueError("Invalid value for `parameter_assignments`, must not be `None`")  # noqa: E501

        self._parameter_assignments = parameter_assignments

    @property
    def primary_container_name(self):
        """Gets the primary_container_name of this V1beta1TrialSpec.  # noqa: E501

        Name of training container where actual model training is running  # noqa: E501

        :return: The primary_container_name of this V1beta1TrialSpec.  # noqa: E501
        :rtype: str
        """
        return self._primary_container_name

    @primary_container_name.setter
    def primary_container_name(self, primary_container_name):
        """Sets the primary_container_name of this V1beta1TrialSpec.

        Name of training container where actual model training is running  # noqa: E501

        :param primary_container_name: The primary_container_name of this V1beta1TrialSpec.  # noqa: E501
        :type: str
        """

        self._primary_container_name = primary_container_name

    @property
    def primary_pod_labels(self):
        """Gets the primary_pod_labels of this V1beta1TrialSpec.  # noqa: E501

        Label that determines if pod needs to be injected by Katib sidecar container  # noqa: E501

        :return: The primary_pod_labels of this V1beta1TrialSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._primary_pod_labels

    @primary_pod_labels.setter
    def primary_pod_labels(self, primary_pod_labels):
        """Sets the primary_pod_labels of this V1beta1TrialSpec.

        Label that determines if pod needs to be injected by Katib sidecar container  # noqa: E501

        :param primary_pod_labels: The primary_pod_labels of this V1beta1TrialSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._primary_pod_labels = primary_pod_labels

    @property
    def retain_run(self):
        """Gets the retain_run of this V1beta1TrialSpec.  # noqa: E501

        Whether to retain the trial run object after completed.  # noqa: E501

        :return: The retain_run of this V1beta1TrialSpec.  # noqa: E501
        :rtype: bool
        """
        return self._retain_run

    @retain_run.setter
    def retain_run(self, retain_run):
        """Sets the retain_run of this V1beta1TrialSpec.

        Whether to retain the trial run object after completed.  # noqa: E501

        :param retain_run: The retain_run of this V1beta1TrialSpec.  # noqa: E501
        :type: bool
        """

        self._retain_run = retain_run

    @property
    def run_spec(self):
        """Gets the run_spec of this V1beta1TrialSpec.  # noqa: E501

        Raw text for the trial run spec. This can be any generic Kubernetes runtime object. The trial operator should create the resource as written, and let the corresponding resource controller (e.g. tf-operator) handle the rest.  # noqa: E501

        :return: The run_spec of this V1beta1TrialSpec.  # noqa: E501
        :rtype: V1UnstructuredUnstructured
        """
        return self._run_spec

    @run_spec.setter
    def run_spec(self, run_spec):
        """Sets the run_spec of this V1beta1TrialSpec.

        Raw text for the trial run spec. This can be any generic Kubernetes runtime object. The trial operator should create the resource as written, and let the corresponding resource controller (e.g. tf-operator) handle the rest.  # noqa: E501

        :param run_spec: The run_spec of this V1beta1TrialSpec.  # noqa: E501
        :type: V1UnstructuredUnstructured
        """

        self._run_spec = run_spec

    @property
    def success_condition(self):
        """Gets the success_condition of this V1beta1TrialSpec.  # noqa: E501

        Condition when trial custom resource is succeeded. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Complete\")#|#(status==\"True\")#  # noqa: E501

        :return: The success_condition of this V1beta1TrialSpec.  # noqa: E501
        :rtype: str
        """
        return self._success_condition

    @success_condition.setter
    def success_condition(self, success_condition):
        """Sets the success_condition of this V1beta1TrialSpec.

        Condition when trial custom resource is succeeded. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Complete\")#|#(status==\"True\")#  # noqa: E501

        :param success_condition: The success_condition of this V1beta1TrialSpec.  # noqa: E501
        :type: str
        """

        self._success_condition = success_condition

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1beta1TrialSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1TrialSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
