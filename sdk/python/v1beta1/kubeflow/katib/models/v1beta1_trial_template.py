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
from kubeflow.katib.models.v1beta1_config_map_source import V1beta1ConfigMapSource  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_trial_parameter_spec import V1beta1TrialParameterSpec  # noqa: F401,E501


class V1beta1TrialTemplate(object):
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
        'config_map': 'V1beta1ConfigMapSource',
        'failure_condition': 'str',
        'primary_container_name': 'str',
        'primary_pod_labels': 'dict(str, str)',
        'retain': 'bool',
        'success_condition': 'str',
        'trial_parameters': 'list[V1beta1TrialParameterSpec]',
        'trial_spec': 'V1UnstructuredUnstructured'
    }

    attribute_map = {
        'config_map': 'configMap',
        'failure_condition': 'failureCondition',
        'primary_container_name': 'primaryContainerName',
        'primary_pod_labels': 'primaryPodLabels',
        'retain': 'retain',
        'success_condition': 'successCondition',
        'trial_parameters': 'trialParameters',
        'trial_spec': 'trialSpec'
    }

    def __init__(self, config_map=None, failure_condition=None, primary_container_name=None, primary_pod_labels=None, retain=None, success_condition=None, trial_parameters=None, trial_spec=None):  # noqa: E501
        """V1beta1TrialTemplate - a model defined in Swagger"""  # noqa: E501

        self._config_map = None
        self._failure_condition = None
        self._primary_container_name = None
        self._primary_pod_labels = None
        self._retain = None
        self._success_condition = None
        self._trial_parameters = None
        self._trial_spec = None
        self.discriminator = None

        if config_map is not None:
            self.config_map = config_map
        if failure_condition is not None:
            self.failure_condition = failure_condition
        if primary_container_name is not None:
            self.primary_container_name = primary_container_name
        if primary_pod_labels is not None:
            self.primary_pod_labels = primary_pod_labels
        if retain is not None:
            self.retain = retain
        if success_condition is not None:
            self.success_condition = success_condition
        if trial_parameters is not None:
            self.trial_parameters = trial_parameters
        if trial_spec is not None:
            self.trial_spec = trial_spec

    @property
    def config_map(self):
        """Gets the config_map of this V1beta1TrialTemplate.  # noqa: E501

        ConfigMap spec represents a reference to ConfigMap  # noqa: E501

        :return: The config_map of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: V1beta1ConfigMapSource
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this V1beta1TrialTemplate.

        ConfigMap spec represents a reference to ConfigMap  # noqa: E501

        :param config_map: The config_map of this V1beta1TrialTemplate.  # noqa: E501
        :type: V1beta1ConfigMapSource
        """

        self._config_map = config_map

    @property
    def failure_condition(self):
        """Gets the failure_condition of this V1beta1TrialTemplate.  # noqa: E501

        Condition when trial custom resource is failed. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Failed\")#|#(status==\"True\")#  # noqa: E501

        :return: The failure_condition of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: str
        """
        return self._failure_condition

    @failure_condition.setter
    def failure_condition(self, failure_condition):
        """Sets the failure_condition of this V1beta1TrialTemplate.

        Condition when trial custom resource is failed. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Failed\")#|#(status==\"True\")#  # noqa: E501

        :param failure_condition: The failure_condition of this V1beta1TrialTemplate.  # noqa: E501
        :type: str
        """

        self._failure_condition = failure_condition

    @property
    def primary_container_name(self):
        """Gets the primary_container_name of this V1beta1TrialTemplate.  # noqa: E501

        Name of training container where actual model training is running  # noqa: E501

        :return: The primary_container_name of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: str
        """
        return self._primary_container_name

    @primary_container_name.setter
    def primary_container_name(self, primary_container_name):
        """Sets the primary_container_name of this V1beta1TrialTemplate.

        Name of training container where actual model training is running  # noqa: E501

        :param primary_container_name: The primary_container_name of this V1beta1TrialTemplate.  # noqa: E501
        :type: str
        """

        self._primary_container_name = primary_container_name

    @property
    def primary_pod_labels(self):
        """Gets the primary_pod_labels of this V1beta1TrialTemplate.  # noqa: E501

        Labels that determines if pod needs to be injected by Katib sidecar container  # noqa: E501

        :return: The primary_pod_labels of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._primary_pod_labels

    @primary_pod_labels.setter
    def primary_pod_labels(self, primary_pod_labels):
        """Sets the primary_pod_labels of this V1beta1TrialTemplate.

        Labels that determines if pod needs to be injected by Katib sidecar container  # noqa: E501

        :param primary_pod_labels: The primary_pod_labels of this V1beta1TrialTemplate.  # noqa: E501
        :type: dict(str, str)
        """

        self._primary_pod_labels = primary_pod_labels

    @property
    def retain(self):
        """Gets the retain of this V1beta1TrialTemplate.  # noqa: E501

        Retain indicates that trial resources must be not cleanup  # noqa: E501

        :return: The retain of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._retain

    @retain.setter
    def retain(self, retain):
        """Sets the retain of this V1beta1TrialTemplate.

        Retain indicates that trial resources must be not cleanup  # noqa: E501

        :param retain: The retain of this V1beta1TrialTemplate.  # noqa: E501
        :type: bool
        """

        self._retain = retain

    @property
    def success_condition(self):
        """Gets the success_condition of this V1beta1TrialTemplate.  # noqa: E501

        Condition when trial custom resource is succeeded. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Complete\")#|#(status==\"True\")#  # noqa: E501

        :return: The success_condition of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: str
        """
        return self._success_condition

    @success_condition.setter
    def success_condition(self, success_condition):
        """Sets the success_condition of this V1beta1TrialTemplate.

        Condition when trial custom resource is succeeded. Condition must be in GJSON format, ref https://github.com/tidwall/gjson. For example for BatchJob: status.conditions.#(type==\"Complete\")#|#(status==\"True\")#  # noqa: E501

        :param success_condition: The success_condition of this V1beta1TrialTemplate.  # noqa: E501
        :type: str
        """

        self._success_condition = success_condition

    @property
    def trial_parameters(self):
        """Gets the trial_parameters of this V1beta1TrialTemplate.  # noqa: E501

        List of parameters that are used in trial template  # noqa: E501

        :return: The trial_parameters of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: list[V1beta1TrialParameterSpec]
        """
        return self._trial_parameters

    @trial_parameters.setter
    def trial_parameters(self, trial_parameters):
        """Sets the trial_parameters of this V1beta1TrialTemplate.

        List of parameters that are used in trial template  # noqa: E501

        :param trial_parameters: The trial_parameters of this V1beta1TrialTemplate.  # noqa: E501
        :type: list[V1beta1TrialParameterSpec]
        """

        self._trial_parameters = trial_parameters

    @property
    def trial_spec(self):
        """Gets the trial_spec of this V1beta1TrialTemplate.  # noqa: E501

        TrialSpec represents trial template in unstructured format  # noqa: E501

        :return: The trial_spec of this V1beta1TrialTemplate.  # noqa: E501
        :rtype: V1UnstructuredUnstructured
        """
        return self._trial_spec

    @trial_spec.setter
    def trial_spec(self, trial_spec):
        """Sets the trial_spec of this V1beta1TrialTemplate.

        TrialSpec represents trial template in unstructured format  # noqa: E501

        :param trial_spec: The trial_spec of this V1beta1TrialTemplate.  # noqa: E501
        :type: V1UnstructuredUnstructured
        """

        self._trial_spec = trial_spec

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
        if issubclass(V1beta1TrialTemplate, dict):
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
        if not isinstance(other, V1beta1TrialTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
