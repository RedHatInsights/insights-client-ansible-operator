#!/bin/bash

export OPERATOR_NAME=insights-client-ansible-operator
operator-sdk up local --watches-file=watches.local.yaml --namespace=default --kubeconfig=$HOME/jjaggars-test-cluster/auth/kubeconfig 2>&1 | ./lawg.py
