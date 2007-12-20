#include "PhysicsTools/Utilities/src/ExpressionVarSetter.h"
#include "PhysicsTools/Utilities/src/ExpressionVar.h"
#include "PhysicsTools/Utilities/src/findMethod.h"
#include "PhysicsTools/Utilities/src/returnType.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include <string>
#include <iostream>
using namespace reco::parser;
using namespace std;
using namespace ROOT::Reflex;

void ExpressionVarSetter::operator()(const char * begin, const char* end) const {
  cerr << ">>> creating expression" << endl;
  Type type = typeStack_.back();
  method::TypeCode retType = reco::typeCode(type);
  if(retType == method::invalid)
    throw  edm::Exception(edm::errors::Configuration)
      << "member " << methStack_.back().method().Name() << " has an invalid return type: \"" 
      <<  methStack_.back().method().TypeOf().Name() << "\"\n";
  cerr << ">>> methods: " << methStack_.size() << endl;
  exprStack_.push_back(boost::shared_ptr<ExpressionBase>(new ExpressionVar(methStack_, retType)));
  methStack_.clear();
  typeStack_.resize(1);
}
