SUBDIRS = probability hmms gmm-em ising-gibbs

# Phony target to build subdirectories
.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@
